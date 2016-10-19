{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE LambdaCase #-}
module FunctionsOrNot(runTests) where
import           Debug.Trace
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    lines' = map (map (read::String -> Int) . words). lines $ input
    testCases = unfoldr (\case [n]:t -> Just (splitAt n t); _ -> Nothing) $ drop 1 lines'
    f testCase = all not [(a1 == b1) && (a2 /= b2) | [a1, a2] <- testCase, [b1, b2] <- testCase]
    output = unlines . map ((\case True -> "YES"; _ -> "NO") . f) $ testCases

unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
unfoldr f s = maybe [] (\(a, b) -> a:unfoldr f b) $ f s

prop_run = run "2\n\
\3\n\
\1 1\n\
\2 2\n\
\3 3\n\
\4\n\
\1 2\n\
\2 4\n\
\3 6\n\
\4 8\n" == "YES\n\
\YES\n"

return []
runTests = $quickCheckAll
