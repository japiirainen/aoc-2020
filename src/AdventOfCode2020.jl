module AdventOfCode2020

function readinput(day::Number, parser)
    f = open("input/$day.txt", "r")
    contents = read(f, String)
    parser(contents)
end
export readinput

lines(xs::String) = split(xs, "\n")
export lines

ints(xs::String) = [parse(Int, x) for x ∈ lines(xs)]
export ints

end # module
