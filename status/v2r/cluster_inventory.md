# V2R cluster inventory

2026-09-24T03:45:15.983993+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324743020544 available bytes; 81.88% used; 112493728 free inodes.

server1 `/home`: 324743020544 available bytes; 81.88% used; 112493728 free inodes.

server1 `/tmp`: 324743020544 available bytes; 81.88% used; 112493728 free inodes.

server1 `/var/tmp`: 324743020544 available bytes; 81.88% used; 112493728 free inodes.

server1 `/mnt/raid5`: 402122645504 available bytes; 98.16% used; 337724833 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40826515456 available bytes; 97.72% used; 110430980 free inodes.

server2 `/home`: 40826515456 available bytes; 97.72% used; 110430980 free inodes.

server2 `/tmp`: 40826515456 available bytes; 97.72% used; 110430980 free inodes.

server2 `/var/tmp`: 40826515456 available bytes; 97.72% used; 110430980 free inodes.

server2 `/mnt/raid5`: 526749007872 available bytes; 96.36% used; 445197455 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292367454208 available bytes; 83.68% used; 114197838 free inodes.

server3 `/home`: 292367454208 available bytes; 83.68% used; 114197838 free inodes.

server3 `/data`: 33879089152 available bytes; 99.53% used; 225842700 free inodes.

server3 `/tmp`: 292367454208 available bytes; 83.68% used; 114197838 free inodes.

server3 `/var/tmp`: 292367454208 available bytes; 83.68% used; 114197838 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105792802816 available bytes; 94.10% used; 114349566 free inodes.

server4 `/home`: 105792802816 available bytes; 94.10% used; 114349566 free inodes.

server4 `/data`: 277153202176 available bytes; 96.17% used; 225384265 free inodes.

server4 `/tmp`: 105792802816 available bytes; 94.10% used; 114349566 free inodes.

server4 `/var/tmp`: 105792802816 available bytes; 94.10% used; 114349566 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
