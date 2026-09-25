# V2R cluster inventory

2026-09-25T04:43:49.754302+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318914793472 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318914793472 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318914793472 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318914793472 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 408693596160 available bytes; 98.13% used; 337590017 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22948487168 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22948487168 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22948487168 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22948487168 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 462078939136 available bytes; 96.81% used; 445109376 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340166656 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84340166656 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143293251584 available bytes; 98.02% used; 225815888 free inodes.

server3 `/tmp`: 84340166656 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84340166656 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105663918080 available bytes; 94.10% used; 114350594 free inodes.

server4 `/home`: 105663918080 available bytes; 94.10% used; 114350594 free inodes.

server4 `/data`: 31170977792 available bytes; 99.57% used; 224962213 free inodes.

server4 `/tmp`: 105663918080 available bytes; 94.10% used; 114350594 free inodes.

server4 `/var/tmp`: 105663918080 available bytes; 94.10% used; 114350594 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
