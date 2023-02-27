module Day02

using AdventOfCode2020

struct Passport
    policy::Tuple{Int,Int,Char}
    passport::String
    validitycheck::Function
    Passport(policy, passport, validitycheck) = validitycheck(policy, passport) ? new(policy, passport) : error("Invalid Passport")
end

function parsepassports(validitycheck, ls)
    pps = []
    for l ∈ ls
        try
            policy, passport = split(l, ": ")
            lo, rest = split(policy, "-")
            hi, c = split(rest, " ")
            push!(pps, Passport((parse(Int, lo), parse(Int, hi), only(c)), passport, validitycheck))
        catch
        end
    end
    pps
end

I = readinput(2, lines)

solve(p, ls) = parsepassports(p, ls) |> length


function valid1((lo, hi, c), passport)
    cc = [1 for char in passport if char == c] |> sum
    cc >= lo && cc <= hi
end

# Part 1
solve(valid1, I)

function valid2((p1, p2, c), passport)
    at1 = passport[p1] == c
    at2 = passport[p2] == c
    at1 && !at2 || at2 && !at1
end

# Part 2
solve(valid2, I)

end # module