{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE LambdaCase #-}
module StringOPermute(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All
import           Debug.Trace

main :: IO ()
main = interact run

run :: String -> String
run input = trace output output where
    testCases = drop 1 . lines $ input
    f = concat . unfoldr (\case a:b:line' -> Just ([b, a], line'); _ -> Nothing)
    output = unlines . map f $ testCases

unfoldr :: (t1 -> Maybe (t, t1)) -> t1 -> [t]
unfoldr f b = maybe [] (\(a, b') -> a:unfoldr f b') (f b)

prop_run = run "\
\2\n\
\abcdpqrs\n\
\az\n\
\" == "\
\badcqpsr\n\
\za\n\
\"

return []
runTests = $quickCheckAll
