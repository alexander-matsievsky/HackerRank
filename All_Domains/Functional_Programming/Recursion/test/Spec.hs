import           FunctionalProgrammingWarmupsInRecursionFibonacciNumbers
import           FunctionalProgrammingWarmupsInRecursionGcd
import           PascalsTriangle

main = do
    _ <- FunctionalProgrammingWarmupsInRecursionGcd.runTests
    _ <- FunctionalProgrammingWarmupsInRecursionFibonacciNumbers.runTests
    _ <- PascalsTriangle.runTests
    return ()
