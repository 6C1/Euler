
def main(): Int = {

  def loop(secondToLast: Int = 0, last: Int = 1, sum: Int = 0): Int = {
    secondToLast + last match {
      case c if c % 2 == 0 && c < 4000000 => loop(last, c, c + sum)
      case c if c < 4000000 => loop(last, c, sum)
      case _ => sum
    }
  }

  loop()
}

println(main())
