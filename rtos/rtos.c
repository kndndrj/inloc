#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#define F_CPU 8000000UL  
#include <util/delay.h>

typedef struct task {
   unsigned char running; // 1 indicates task is running
   int state;             // Current state of state machine
   unsigned long period; // Rate at which the task should tick
   unsigned long elapsedTime; // Time since task's previous tick
   int (*TickFct)(int); // Function to call for task's tick
} task;

task tasks[3];

const unsigned char tasksNum = 3;
const unsigned long tasksPeriodGCD = 25;
const unsigned long period1 = 1000;
const unsigned long period2 = 2000;
const unsigned long period3 = 3000;

int TickFct_1(int state);
int TickFct_2(int state);
int TickFct_3(int state);

unsigned char runningTasks[4] = {255}; // Track running tasks, [0] always idleTask
const unsigned long idleTask = 255; // 0 highest priority, 255 lowest
unsigned char currentTask = 0; // Index of highest priority task in runningTasks

unsigned schedule_time = 0;
ISR(TIMER1_COMPA_vect) {
   unsigned char i;
   for (i=0; i < tasksNum; ++i) { // Heart of scheduler code
      if (  (tasks[i].elapsedTime >= tasks[i].period) // Task ready
          && (runningTasks[currentTask] > i) // Task priority > current task priority
          && (!tasks[i].running) // Task not already running (no self-preemption)
         ) { 
         SREG &= 0x7F;
         tasks[i].elapsedTime = 0; // Reset time since last tick
         tasks[i].running = 1; // Mark as running
         currentTask += 1;
         runningTasks[currentTask] = i; // Add to runningTasks
         SREG |= 0x80;
         
         tasks[i].state = tasks[i].TickFct(tasks[i].state); // Execute tick
         
         SREG &= 0x7F;
         tasks[i].running = 0; // Mark as not running
         runningTasks[currentTask] = idleTask; // Remove from runningTasks
         currentTask -= 1;
         SREG |= 0x80;
      }
      tasks[i].elapsedTime += tasksPeriodGCD;
   }
}

void init_processor() {
    
    /*Set up SPI*/
    PORTB = 0xff;
    
    /*Set up timer*/
    TCCR1B = (1<<WGM12)|(1<<CS11); // CTC mode (clear timer on compare). Prescaler=8
    // AVR output compare register OCR0.
    OCR1A = 25000;
    // AVR timer interrupt mask register         
    TIMSK1 = (1<<OCIE1A); //enables compare match interrupt
    TCNT1 = 0;

    /*Init GPIO pins PB0, PB1, PB2*/
    DDRB |= _BV(DDB0); 
    DDRB |= _BV(DDB1); 
    DDRB |= _BV(DDB2); 
        
    /*Enable global interrupts*/
    SREG |= 0x80;
}

int main(void)
{
    init_processor();

   // Priority assigned to lower position tasks in array
   unsigned char i = 0;
   tasks[i].state = -1;
   tasks[i].period = period1;
   tasks[i].elapsedTime = tasks[i].period;
   tasks[i].running = 0;
   tasks[i].TickFct = &TickFct_1;
   ++i;
   tasks[i].state = -1;
   tasks[i].period = period2;
   tasks[i].elapsedTime = tasks[i].period;
   tasks[i].running = 0;
   tasks[i].TickFct = &TickFct_2;
   ++i;
   tasks[i].state = -1;
   tasks[i].period = period3;
   tasks[i].elapsedTime = tasks[i].period;
   tasks[i].running = 0;
   tasks[i].TickFct = &TickFct_3;
    
    while(1)
    {
    }
}

int TickFct_1(int state) {
    PORTB ^= _BV(PB0);
    return 0;
}

int TickFct_2(int state) {
    PORTB ^= _BV(PB1);
    return 0;
}

int TickFct_3(int state) {
    PORTB ^= _BV(PB2);
    return 0;
}
