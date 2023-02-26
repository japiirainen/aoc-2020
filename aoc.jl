### A Pluto.jl notebook ###
# v0.19.22

using Markdown
using InteractiveUtils

# ╔═╡ 9944a528-1f84-4956-b12e-f85fea253da7
md"""
# Advent Of Code 2020

In the year 2020 I will attempt to solve the problems in Julia, which I have *never* touched before. Let's see how far I'll make it.
"""

# ╔═╡ 4ccb8d4a-8dcd-44f6-b5b7-4b6d0a870985
begin
	function readinput(day, parser)
		f = open("input/$day.txt", "r")
		contents = read(f, String)
		parser(contents)
	end
	
	lines(xs) = split(xs, "\n")

	ints(xs) = [parse(Int, x) for x ∈ lines(xs)]
end

# ╔═╡ 9c4319d2-5b03-4752-aa25-978b5352a16d
md"""
## Day 1
"""

# ╔═╡ beb7618b-4578-49aa-963e-6c9db6b7e0a5
in1 = readinput(1, ints) |> Set

# ╔═╡ d9d89c8c-7a7f-4a11-a71f-7611ffe84043
md"""
### Part 1

In part 1 of day 1 we are asked to find two distinct numbers from the input, which when added up $\equiv$ 2020. Once we find those numbers we are asked to ad them up.
"""

# ╔═╡ fed0e58c-e293-4f4a-b43c-b5d0f105b5a2
[a*b for a ∈ in1 for b ∈ in1 ∩ (2020-a)] |> first

# ╔═╡ 2117a9e4-c4d7-40f9-b277-7efe3cba0ead
md"""
### Part 2

In part 2 we need to do the same dance but with 3 numbers.
"""

# ╔═╡ 36edb5c0-1580-442d-9a4b-7c3e5c22e3f9
[a*b*c for a ∈ in1 for b ∈ in1 for c ∈ in1 ∩ (2020-a-b)] |> first

# ╔═╡ a32e71c7-9c88-4692-a756-318f955e7f8e
md"""
## Day 2
"""

# ╔═╡ 6cb99944-c357-43bd-876a-5e7ba3b84182
md"""
Seems like we ned to do some parsing this time.

I decided to solve the problem almost entirely in the parsing phase. Julia Constructors seemed like a nice fit for this kind of input validation. The only thing I don't like about this solution is the fact that I need to throw in the case validation fails. I wonder if there's some nicer way to handle this...

Btw this Julia Constructor pattern reminds me of the [Smart Constructor](https://wiki.haskell.org/Smart_constructors) pattern.

Anyway, the only difference between part 1 and 2 was in the passport validation logic.
"""

# ╔═╡ 39241651-876f-4e79-bb52-154acddd6b0d
begin
	struct Passport
		policy::Tuple{Int, Int, Char}
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
	in2 = readinput(2, lines)
	solve(p, ls) = parsepassports(p, ls) |> length
end

# ╔═╡ 42ecef71-bbd6-40e5-8f49-f873a6116d73
md"""
### Part 1
"""

# ╔═╡ 9ff40049-2516-40bc-8804-34237d33fe6d
begin
	function validpp1((lo, hi, c), passport)
		cc = [1 for char in passport if char == c] |> sum
		cc >= lo && cc <= hi
	end
	solve(validpp1, in2)
end

# ╔═╡ 0daf88c2-b0e8-433f-bdde-6f3f57861912
md"""
### Part 2
"""

# ╔═╡ 75f408b5-3f5b-4f12-978a-9be80a0afc59
begin
	function validpp2((p1, p2, c), passport)
		at1 = passport[p1] == c
		at2 = passport[p2] == c
		at1 && !at2 || at2 && !at1
	end
	solve(validpp2, in2)
end

# ╔═╡ Cell order:
# ╠═9944a528-1f84-4956-b12e-f85fea253da7
# ╠═4ccb8d4a-8dcd-44f6-b5b7-4b6d0a870985
# ╠═9c4319d2-5b03-4752-aa25-978b5352a16d
# ╠═beb7618b-4578-49aa-963e-6c9db6b7e0a5
# ╠═d9d89c8c-7a7f-4a11-a71f-7611ffe84043
# ╠═fed0e58c-e293-4f4a-b43c-b5d0f105b5a2
# ╠═2117a9e4-c4d7-40f9-b277-7efe3cba0ead
# ╠═36edb5c0-1580-442d-9a4b-7c3e5c22e3f9
# ╠═a32e71c7-9c88-4692-a756-318f955e7f8e
# ╠═6cb99944-c357-43bd-876a-5e7ba3b84182
# ╠═39241651-876f-4e79-bb52-154acddd6b0d
# ╠═42ecef71-bbd6-40e5-8f49-f873a6116d73
# ╠═9ff40049-2516-40bc-8804-34237d33fe6d
# ╠═0daf88c2-b0e8-433f-bdde-6f3f57861912
# ╠═75f408b5-3f5b-4f12-978a-9be80a0afc59
