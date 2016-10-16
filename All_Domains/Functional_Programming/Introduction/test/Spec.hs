import           FpArrayOfNElements
import           FpFilterArray
import           FpFilterPositionsInAList
import           FpHelloWorld
import           FpHelloWorldNTimes
import           FpListReplication
import           FpReverseAList
import           FpSolveMeFirst
import           FpSumOfOddElements
import           FpListLength

main = do
    _ <- FpSolveMeFirst.runTests
    _ <- FpHelloWorld.runTests
    _ <- FpHelloWorldNTimes.runTests
    _ <- FpListReplication.runTests
    _ <- FpFilterArray.runTests
    _ <- FpFilterPositionsInAList.runTests
    _ <- FpArrayOfNElements.runTests
    _ <- FpReverseAList.runTests
    _ <- FpSumOfOddElements.runTests
    _ <- FpListLength.runTests
    return ()
