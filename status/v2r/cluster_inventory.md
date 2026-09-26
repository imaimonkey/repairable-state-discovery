# V2R cluster inventory

2026-09-26T09:43:51.248732+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318616510464 available bytes; 82.23% used; 112475072 free inodes.

server1 `/home`: 318616510464 available bytes; 82.23% used; 112475072 free inodes.

server1 `/tmp`: 318616510464 available bytes; 82.23% used; 112475072 free inodes.

server1 `/var/tmp`: 318616510464 available bytes; 82.23% used; 112475072 free inodes.

server1 `/mnt/raid5`: 218935865344 available bytes; 99.00% used; 337538580 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22316392448 available bytes; 98.76% used; 110403892 free inodes.

server2 `/home`: 22316392448 available bytes; 98.76% used; 110403892 free inodes.

server2 `/tmp`: 22316392448 available bytes; 98.76% used; 110403892 free inodes.

server2 `/var/tmp`: 22316392448 available bytes; 98.76% used; 110403892 free inodes.

server2 `/mnt/raid5`: 253794811904 available bytes; 98.25% used; 445022350 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82658623488 available bytes; 95.39% used; 114110795 free inodes.

server3 `/home`: 82658623488 available bytes; 95.39% used; 114110795 free inodes.

server3 `/data`: 123592556544 available bytes; 98.29% used; 225827566 free inodes.

server3 `/tmp`: 82658623488 available bytes; 95.39% used; 114110795 free inodes.

server3 `/var/tmp`: 82658623488 available bytes; 95.39% used; 114110795 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105932296192 available bytes; 94.09% used; 114348032 free inodes.

server4 `/home`: 105932296192 available bytes; 94.09% used; 114348032 free inodes.

server4 `/data`: 89268772864 available bytes; 98.77% used; 224882598 free inodes.

server4 `/tmp`: 105932296192 available bytes; 94.09% used; 114348032 free inodes.

server4 `/var/tmp`: 105932296192 available bytes; 94.09% used; 114348032 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
