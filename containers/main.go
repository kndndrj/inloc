package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {
	switch os.Args[1] {
	case "run":
		parent()
	case "__child":
		child()
	default:
		panic("what should I do?")
	}
}

func parent() {
	cmd := exec.Command("/proc/self/exe", append([]string{"__child"}, os.Args[2:]...)...)
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS,
	}
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	must(cmd.Run())
}

func child() {
	must(syscall.Chroot("./rootfs"))
	must(os.Chdir("/"))
	must(syscall.Mount("proc", "proc", "proc", 0, ""))

	cmd := exec.Command(os.Args[2], os.Args[3:]...)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	must(cmd.Run())
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
