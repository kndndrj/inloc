# Projects `In N Lines Of Code`

This repository contains various small projects, which help understand complex topics.

The projects themselves are as small as possible to illustrate the point.

All projects from the `master` branch are featured in
[my series on youtube](https://youtube.com/playlist?list=PLspLRijkVjGCFD5iXY2LYhclbypwipizE)!

## Contributing

If you have an example which fits this repository, please consider opening a pull request.

Each example should have it's own pull request. The file structure of the added example should look
aproximately like this:

```
<folder name>/          # A new top-level folder - name of the folder should
                        # be contextual, not tied to a specific project
                        # name (example: `compiler` not `tinyc`).
    <source_file_1>
    <source_file_2>
    <source_file_...>
    README.md           # See below.
```

The `README.md` should have the following structure. `Lines of Code` field shouldn't contain empty
and comment lines. I suggest that you determine the number using
[`cloc`](https://github.com/AlDanial/cloc).

```
# <Title>

|  Language  | Lines of Code |
| :--------: | :-----------: |
| <language> |     <loc>     |

<optional description>

## Running

<instractions on how to run the code>

## Sources

<list of sources of the example>

## License

<license of the example(s)>
```

## License

Everything not mentioned in `README.md` files in subfolders is licensed under
[MIT license](./LICENSE)
