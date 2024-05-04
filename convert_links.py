import sys

with open(sys.argv[1]) as infile:
    lines = infile.readlines()

with open(sys.argv[1], "w") as outfile:
    for line in lines:
        new_line = ""

        # go through line, index by index, and find/replace
        t_start = 0
        while t_start < len(line):
            if line[t_start] != "[":
                new_line += line[t_start]

            # open bracket
            else:
                t_end = line.find("]", t_start)
                l_start = t_end + 1

                # exclude special case "](#" for in-post links
                if l_start < len(line) and line[l_start] == "(" and line[l_start+1] != "#":
                    l_end = line.find(")", l_start)

                    text = line[t_start+1:t_end]
                    link = line[l_start+1:l_end]

                    # convert '[text](link.com)' to '<a target="_blank" href="link.com">text</a>'
                    temp = "<a target=\"_blank\" href=\"{link}\">{text}</a>"
                    new_link_text = temp.format(link=link, text=text)

                    new_line += new_link_text
                    t_start = l_end

                # found a closed bracket, but we're not dealing with a link
                else:
                    new_line += line[t_start:t_end+1]
                    t_start = t_end

            t_start += 1

        outfile.write(new_line)

print("Done!")
