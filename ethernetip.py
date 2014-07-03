def add_point_to_ip( ip_addr ) :
    """This function accepts a 12 hex digit string and converts it to a colon separated string"""
    s = list()
    for i in range(8/2) :       # mac_addr should always be 12 chars, we work in groups of 2 chars
        s.append( int(ip_addr[i*2:i*2+2],16) )
    r = str(s[0]).strip() + "." + str(s[1]).strip() + "." + str(s[2]).strip() + "." + str(s[3]).strip()
    return r
