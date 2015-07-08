
def main(): Int = {

  def loop(secondToLast: Int = 0, last: Int = 1, sum: Int = 0): Int = {
    val curr = secondToLast + last
    if (curr < 4000000) {
      if (curr % 2 == 0) loop(last, curr, sum + curr)
      else loop(last, curr, sum)
    } else sum
  }

  loop()
}

println(main())
