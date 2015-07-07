var total = 0

for (i <- 0 to 1000) {
  if (i % 3 == 0 || i % 5 == 0) total += i
}

println(total)
