module Day01

using AdventOfCode2020

I = readinput(1, ints) |> Set

# Part 1
[a * b for a ∈ I for b ∈ I ∩ (2020 - a)] |> first

# Part 2
[a * b * c for a ∈ I for b ∈ I for c ∈ I ∩ (2020 - a - b)] |> first

end # module