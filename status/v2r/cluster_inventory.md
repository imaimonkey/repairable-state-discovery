# V2R cluster inventory

2026-09-25T11:50:18.415456+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319047462912 available bytes; 82.20% used; 112478818 free inodes.

server1 `/home`: 319047462912 available bytes; 82.20% used; 112478818 free inodes.

server1 `/tmp`: 319047462912 available bytes; 82.20% used; 112478818 free inodes.

server1 `/var/tmp`: 319047462912 available bytes; 82.20% used; 112478818 free inodes.

server1 `/mnt/raid5`: 369868242944 available bytes; 98.30% used; 337549224 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22905778176 available bytes; 98.72% used; 110409974 free inodes.

server2 `/home`: 22905778176 available bytes; 98.72% used; 110409974 free inodes.

server2 `/tmp`: 22905778176 available bytes; 98.72% used; 110409974 free inodes.

server2 `/var/tmp`: 22905778176 available bytes; 98.72% used; 110409974 free inodes.

server2 `/mnt/raid5`: 326511673344 available bytes; 97.74% used; 445082746 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84214431744 available bytes; 95.30% used; 114154984 free inodes.

server3 `/home`: 84214431744 available bytes; 95.30% used; 114154984 free inodes.

server3 `/data`: 142042587136 available bytes; 98.04% used; 225813323 free inodes.

server3 `/tmp`: 84214431744 available bytes; 95.30% used; 114154984 free inodes.

server3 `/var/tmp`: 84214431744 available bytes; 95.30% used; 114154984 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105602506752 available bytes; 94.11% used; 114350231 free inodes.

server4 `/home`: 105602506752 available bytes; 94.11% used; 114350231 free inodes.

server4 `/data`: 232572395520 available bytes; 96.79% used; 224974448 free inodes.

server4 `/tmp`: 105602506752 available bytes; 94.11% used; 114350231 free inodes.

server4 `/var/tmp`: 105602506752 available bytes; 94.11% used; 114350231 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
