# V2R cluster inventory

2026-09-24T06:09:48.949920+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324524130304 available bytes; 81.90% used; 112491844 free inodes.

server1 `/home`: 324524130304 available bytes; 81.90% used; 112491844 free inodes.

server1 `/tmp`: 324524130304 available bytes; 81.90% used; 112491844 free inodes.

server1 `/var/tmp`: 324524130304 available bytes; 81.90% used; 112491844 free inodes.

server1 `/mnt/raid5`: 517602131968 available bytes; 97.63% used; 337723796 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57895219200 available bytes; 96.77% used; 110431270 free inodes.

server2 `/home`: 57895219200 available bytes; 96.77% used; 110431270 free inodes.

server2 `/tmp`: 57895219200 available bytes; 96.77% used; 110431270 free inodes.

server2 `/var/tmp`: 57895219200 available bytes; 96.77% used; 110431270 free inodes.

server2 `/mnt/raid5`: 520868032512 available bytes; 96.40% used; 445192779 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126872530944 available bytes; 92.92% used; 114185471 free inodes.

server3 `/home`: 126872530944 available bytes; 92.92% used; 114185471 free inodes.

server3 `/data`: 161312985088 available bytes; 97.77% used; 225836147 free inodes.

server3 `/tmp`: 126872530944 available bytes; 92.92% used; 114185471 free inodes.

server3 `/var/tmp`: 126872530944 available bytes; 92.92% used; 114185471 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105814986752 available bytes; 94.10% used; 114349319 free inodes.

server4 `/home`: 105814986752 available bytes; 94.10% used; 114349319 free inodes.

server4 `/data`: 339783061504 available bytes; 95.30% used; 225374148 free inodes.

server4 `/tmp`: 105814986752 available bytes; 94.10% used; 114349319 free inodes.

server4 `/var/tmp`: 105814986752 available bytes; 94.10% used; 114349319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
