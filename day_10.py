from collections import namedtuple



Bot = namedtuple("Bot", ['id', 'lo', 'hi', 'chips'])


def move_chips(bot: Bot):
    if len(bot.chips) < 2:
        return
    lo, hi = min(bot.chips), max(bot.chips)
    if lo == 17 and hi == 61:
        print("Solution for part 1: ", bot.id)
    if bot.lo[0] == 'bot':
        bots[bot.lo[1]].chips.append(lo)
        move_chips(bots[bot.lo[1]])
    else:
        if bot.lo[1] in outputs:
            outputs[bot.lo[1]].append(lo)
        else:
            outputs[bot.lo[1]] = [lo]
    if bot.hi[0] == 'bot':
        bots[bot.hi[1]].chips.append(hi)
        move_chips(bots[bot.hi[1]])
    else:
        if bot.hi[1] in outputs:
            outputs[bot.hi[1]].append(hi)
        else:
            outputs[bot.hi[1]] = [hi]
    

if __name__ == "__main__":


    data = open(0).read().splitlines()

    bots = {}
    outputs = {}
    commands = []


    for line in data:
        ln = line.split(" ")
        if ln[0] == 'bot':
            bot = Bot(
                id=int(ln[1]),
                lo=(ln[5], int(ln[6])),
                hi=(ln[10], int(ln[11])),
                chips=[]
            )
            bots[bot.id] = bot
        else:
            commands.append(ln)
    
    for command in commands:
        _, value, _, _, _, bot = command
        bots[int(bot)].chips.append(int(value))
        move_chips(bots[int(bot)])

    
    print("Solution for part 2: ", int(outputs[0][0]) * int(outputs[1][0]) * int(outputs[2][0]))