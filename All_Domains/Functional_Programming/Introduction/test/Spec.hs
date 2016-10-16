import           FpHelloWorld
import           FpHelloWorldNTimes
import           FpSolveMeFirst

main = do
    _ <- FpSolveMeFirst.runTests
    _ <- FpHelloWorld.runTests
    _ <- FpHelloWorldNTimes.runTests
    return ()
