{-# LANGUAGE TemplateHaskell #-}
module FpReverseAList(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    xs = lines input
    output = unlines . rev $ xs

rev :: [t] -> [t]
rev []     = []
rev (x:xs) = rev xs ++ [x]

prop_run = run "19\n\
\22\n\
\3\n\
\28\n\
\26\n\
\17\n\
\18\n\
\4\n\
\28\n\
\0\n" == "0\n\
\28\n\
\4\n\
\18\n\
\17\n\
\26\n\
\28\n\
\3\n\
\22\n\
\19\n"

prop_run2 :: [Integer] -> Bool
prop_run2 xs = (rev . rev $ xs) == xs

prop_run3 :: [Integer] -> Bool
prop_run3 xs = reverse xs == rev xs

return []
runTests = $quickCheckAll
