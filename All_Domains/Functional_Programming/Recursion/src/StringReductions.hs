{-# LANGUAGE LambdaCase      #-}
{-# LANGUAGE TemplateHaskell #-}
module StringReductions(runTests) where
import           Debug.Trace
import           Test.QuickCheck

main :: IO ()
main = interact run

run :: String -> String
run input = trace output output where
    output = foldl step "" input
    step reduction symbol
        | symbol `elem` reduction = reduction
        | otherwise = reduction ++ [symbol]

prop_run = run "accabb" == "acb"
prop_run1 = run "abc" == "abc"
prop_run2 = run "pprrqq" == "prq"

return []
runTests = $quickCheckAll
