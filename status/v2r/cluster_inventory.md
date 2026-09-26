# V2R cluster inventory

2026-09-26T09:40:48.140396+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318617903104 available bytes; 82.23% used; 112475088 free inodes.

server1 `/home`: 318617903104 available bytes; 82.23% used; 112475088 free inodes.

server1 `/tmp`: 318617903104 available bytes; 82.23% used; 112475088 free inodes.

server1 `/var/tmp`: 318617903104 available bytes; 82.23% used; 112475088 free inodes.

server1 `/mnt/raid5`: 218945368064 available bytes; 99.00% used; 337538600 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22317465600 available bytes; 98.75% used; 110403896 free inodes.

server2 `/home`: 22317465600 available bytes; 98.75% used; 110403896 free inodes.

server2 `/tmp`: 22317465600 available bytes; 98.75% used; 110403896 free inodes.

server2 `/var/tmp`: 22317465600 available bytes; 98.75% used; 110403896 free inodes.

server2 `/mnt/raid5`: 253878341632 available bytes; 98.25% used; 445022367 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82655723520 available bytes; 95.39% used; 114110791 free inodes.

server3 `/home`: 82655723520 available bytes; 95.39% used; 114110791 free inodes.

server3 `/data`: 123593744384 available bytes; 98.29% used; 225827613 free inodes.

server3 `/tmp`: 82655723520 available bytes; 95.39% used; 114110791 free inodes.

server3 `/var/tmp`: 82655723520 available bytes; 95.39% used; 114110791 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105934065664 available bytes; 94.09% used; 114348049 free inodes.

server4 `/home`: 105934065664 available bytes; 94.09% used; 114348049 free inodes.

server4 `/data`: 89275576320 available bytes; 98.77% used; 224882594 free inodes.

server4 `/tmp`: 105934065664 available bytes; 94.09% used; 114348049 free inodes.

server4 `/var/tmp`: 105934065664 available bytes; 94.09% used; 114348049 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
