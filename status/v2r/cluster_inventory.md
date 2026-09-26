# V2R cluster inventory

2026-09-26T01:35:21.610305+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318650023936 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318650023936 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318650023936 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318650023936 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 345491013632 available bytes; 98.42% used; 337546520 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940319744 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22940319744 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22940319744 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22940319744 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 290024185856 available bytes; 98.00% used; 445055823 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 84334575616 available bytes; 95.29% used; 114152379 free inodes.

server3 `/home`: 84334575616 available bytes; 95.29% used; 114152379 free inodes.

server3 `/data`: 124799377408 available bytes; 98.28% used; 225817920 free inodes.

server3 `/tmp`: 84334575616 available bytes; 95.29% used; 114152379 free inodes.

server3 `/var/tmp`: 84334575616 available bytes; 95.29% used; 114152379 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105196818432 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196818432 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 134162337792 available bytes; 98.15% used; 224916769 free inodes.

server4 `/tmp`: 105196818432 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196818432 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
