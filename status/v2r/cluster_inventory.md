# V2R cluster inventory

2026-09-26T11:47:27.099290+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318198374400 available bytes; 82.25% used; 112474781 free inodes.

server1 `/home`: 318198374400 available bytes; 82.25% used; 112474781 free inodes.

server1 `/tmp`: 318198374400 available bytes; 82.25% used; 112474781 free inodes.

server1 `/var/tmp`: 318198374400 available bytes; 82.25% used; 112474781 free inodes.

server1 `/mnt/raid5`: 218655674368 available bytes; 99.00% used; 337537996 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19793600512 available bytes; 98.90% used; 110383625 free inodes.

server2 `/home`: 19793600512 available bytes; 98.90% used; 110383625 free inodes.

server2 `/tmp`: 19793600512 available bytes; 98.90% used; 110383625 free inodes.

server2 `/var/tmp`: 19793600512 available bytes; 98.90% used; 110383625 free inodes.

server2 `/mnt/raid5`: 240911323136 available bytes; 98.34% used; 444977418 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82649370624 available bytes; 95.39% used; 114110827 free inodes.

server3 `/home`: 82649370624 available bytes; 95.39% used; 114110827 free inodes.

server3 `/data`: 123431571456 available bytes; 98.29% used; 225825217 free inodes.

server3 `/tmp`: 82649370624 available bytes; 95.39% used; 114110827 free inodes.

server3 `/var/tmp`: 82649370624 available bytes; 95.39% used; 114110827 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105900810240 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105900810240 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88608526336 available bytes; 98.78% used; 224879321 free inodes.

server4 `/tmp`: 105900810240 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105900810240 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
