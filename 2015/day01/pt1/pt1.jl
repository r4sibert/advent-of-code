# Correct solution to day 1 part 1 of AOC, 2015

fpath = "<filepath_to>/input.txt"

function find_santa(path)
    counter = 0
    open(path) do file
        while !eof(file)
            char = read(file, Char)
            if char == '('
                counter += 1
            elseif char == ')'
                counter -= 1
            end
        end 
    end
    return counter
end


println(find_santa(fpath))

