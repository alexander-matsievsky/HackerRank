import           FunctionalProgrammingWarmupsInRecursionFibonacciNumbers
import           FunctionalProgrammingWarmupsInRecursionGcd

main = do
    _ <- FunctionalProgrammingWarmupsInRecursionGcd.runTests
    _ <- FunctionalProgrammingWarmupsInRecursionFibonacciNumbers.runTests
    return ()
