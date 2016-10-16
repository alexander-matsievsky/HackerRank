{-# LANGUAGE TemplateHaskell #-}
module FpArrayOfNElements(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    n = read input
    output = show [1..n]

prop_run = run "3" == "[1,2,3]"

return []
runTests = $quickCheckAll
