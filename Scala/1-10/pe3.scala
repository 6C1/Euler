def factor(n: Long, f: Long = -1, primes: Vector[Long] = Vector(), m: Long = 2): Long = {

  val isPrime = primes.filter(x => x != m).filter(x => m % x == 0).length == 0

  m match {
    case c if m > n => f
    case c if isPrime && n % m == 0 => factor(n/m, m, primes:+m, m)
    case c if isPrime => factor(n, f, primes:+m, m+1)
    case _ => factor(n, f, primes, m+1)
  }

}

println(factor(600851475143L))
