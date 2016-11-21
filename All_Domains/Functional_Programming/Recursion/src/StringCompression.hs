{-# LANGUAGE LambdaCase      #-}
{-# LANGUAGE TemplateHaskell #-}
module StringCompression(runTests) where
import           Data.List
import           Test.QuickCheck

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    output = concatMap print' $ group input
    print' group' = case group' of
        [] -> ""
        [_] -> group'
        letter:_ -> letter : show (length group')

prop_run = run "abcaaabbb" == "abca3b3"
prop_run1 = run "abcd" == "abcd"
prop_run2 = run "aaabaaaaccaaaaba" == "a3ba4c2a4ba"

return []
runTests = $quickCheckAll
