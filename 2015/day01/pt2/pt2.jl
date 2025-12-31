# Correct solution to day 1 part 2 of AOC, 2015 
fpath = "<filepath_to>/input.txt"

function find_santa(path)
    counter = 0
    basement = 0
    open(path) do file
        while basement >=0 && !eof(file)
            char = read(file, Char)
            counter += 1
            if char == '('
                basement += 1
            elseif char == ')'
                basement -= 1
            end
        end 
    end
    return counter 
end


println(find_santa(fpath))

