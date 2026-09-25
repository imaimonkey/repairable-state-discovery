# V2R cluster inventory

2026-09-25T07:26:03.219578+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871646208 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318871646208 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318871646208 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318871646208 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 385911783424 available bytes; 98.23% used; 337558448 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22859907072 available bytes; 98.72% used; 110410498 free inodes.

server2 `/home`: 22859907072 available bytes; 98.72% used; 110410498 free inodes.

server2 `/tmp`: 22859907072 available bytes; 98.72% used; 110410498 free inodes.

server2 `/var/tmp`: 22859907072 available bytes; 98.72% used; 110410498 free inodes.

server2 `/mnt/raid5`: 343361511424 available bytes; 97.63% used; 445097600 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84450369536 available bytes; 95.29% used; 114156025 free inodes.

server3 `/home`: 84450369536 available bytes; 95.29% used; 114156025 free inodes.

server3 `/data`: 142394470400 available bytes; 98.03% used; 225812773 free inodes.

server3 `/tmp`: 84450369536 available bytes; 95.29% used; 114156025 free inodes.

server3 `/var/tmp`: 84450369536 available bytes; 95.29% used; 114156025 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638002688 available bytes; 94.11% used; 114350361 free inodes.

server4 `/home`: 105638002688 available bytes; 94.11% used; 114350361 free inodes.

server4 `/data`: 249104162816 available bytes; 96.56% used; 225014889 free inodes.

server4 `/tmp`: 105638002688 available bytes; 94.11% used; 114350361 free inodes.

server4 `/var/tmp`: 105638002688 available bytes; 94.11% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
