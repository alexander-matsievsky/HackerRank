{-# LANGUAGE TemplateHaskell #-}
module FpSumOfOddElements(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    xs = map read . lines $ input
    output = show . sum . filter odd $ xs

prop_run = run "3\n\
\2\n\
\4\n\
\6\n\
\5\n\
\7\n\
\8\n\
\0\n\
\1\n" == "16"

return []
runTests = $quickCheckAll
