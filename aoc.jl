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

# ╔═╡ Cell order:
# ╠═9944a528-1f84-4956-b12e-f85fea253da7
# ╠═4ccb8d4a-8dcd-44f6-b5b7-4b6d0a870985
# ╠═9c4319d2-5b03-4752-aa25-978b5352a16d
# ╠═beb7618b-4578-49aa-963e-6c9db6b7e0a5
# ╠═d9d89c8c-7a7f-4a11-a71f-7611ffe84043
# ╠═fed0e58c-e293-4f4a-b43c-b5d0f105b5a2
# ╠═2117a9e4-c4d7-40f9-b277-7efe3cba0ead
# ╠═36edb5c0-1580-442d-9a4b-7c3e5c22e3f9
