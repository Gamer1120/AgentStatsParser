from lxml import etree

ENL_PLAYERS=1183
RES_PLAYERS=950

with open("agent_stats.html", 'r') as f:
    data = f.read().replace("\n", "")
    tree = etree.HTML(data)
    r = tree.xpath('//table/thead//td')
    categories = []
    for item in r:
        categories.append(item.text)
    print(categories)
    print(len(categories))
    categorycount_enl = []
    for category in categories:
        categorycount_enl.append(0)
    categorycount_res = []
    for category in categories:
        categorycount_res.append(0)
    #enl players
    #print("Number of ENL players: " + str(len(tree.xpath("//table//tbody/tr[td/@class = 'enl' or td/@class = 'enl recursion-icon']"))))
    for tr in tree.xpath("//table//tbody/tr[td/@class = 'enl' or td/@class = 'enl recursion-icon']"):

        oneplayerstat = etree.HTML(etree.tostring(tr).decode())
        for i in range(3, 36):
            stat = oneplayerstat.xpath("//td")[i].text
            categorycount_enl[i-1] += int(stat.replace(',', ''))
    print(categorycount_enl)
    #res players
    #print("Number of RES players: " + str(len(tree.xpath("//table//tbody/tr[td/@class = 'res' or td/@class = 'res recursion-icon']"))))
    for tr in tree.xpath("//table//tbody/tr[td/@class = 'res' or td/@class = 'res recursion-icon']"):
        oneplayerstat = etree.HTML(etree.tostring(tr).decode())
        for i in range(3, 36):
            stat = oneplayerstat.xpath("//td")[i].text
            categorycount_res[i-1] += int(stat.replace(',', ''))
    print(categorycount_res)
    enl_won = 0
    res_won = 0
    ties = 0
    for i in range(3, 35):
        categorycount_enl[i] = categorycount_enl[i]# / ENL_PLAYERS
        categorycount_res[i] = categorycount_res[i]# / RES_PLAYERS
        print(categories[i] + ": ENL: " + str(round(categorycount_enl[i], 2)) + " RES: " + str(round(categorycount_res[i], 2)))
        if categorycount_enl[i] > categorycount_res[i]:
            enl_won += 1
        elif categorycount_res[i] > categorycount_enl[i]:
            res_won += 1
        else:
            ties += 1
    print("Enlightened won " + str(enl_won) + " categories!")
    print("Resistance won " + str(res_won) + " categories!")
    print("There were ties in " + str(ties) + " categories!")
    # for tr in tree.xpath("//table//tbody/tr[td/@class = 'res' or td/@class = 'res recursion-icon']"):
    #    print(etree.tostring(tr))

