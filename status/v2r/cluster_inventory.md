# V2R cluster inventory

2026-09-24T03:43:03.281915+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324741722112 available bytes; 81.88% used; 112493742 free inodes.

server1 `/home`: 324741722112 available bytes; 81.88% used; 112493742 free inodes.

server1 `/tmp`: 324741722112 available bytes; 81.88% used; 112493742 free inodes.

server1 `/var/tmp`: 324741722112 available bytes; 81.88% used; 112493742 free inodes.

server1 `/mnt/raid5`: 402124771328 available bytes; 98.16% used; 337724835 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40827842560 available bytes; 97.72% used; 110430998 free inodes.

server2 `/home`: 40827842560 available bytes; 97.72% used; 110430998 free inodes.

server2 `/tmp`: 40827842560 available bytes; 97.72% used; 110430998 free inodes.

server2 `/var/tmp`: 40827842560 available bytes; 97.72% used; 110430998 free inodes.

server2 `/mnt/raid5`: 526825717760 available bytes; 96.36% used; 445197534 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291974778880 available bytes; 83.71% used; 114174951 free inodes.

server3 `/home`: 291974778880 available bytes; 83.71% used; 114174951 free inodes.

server3 `/data`: 35995992064 available bytes; 99.50% used; 225842750 free inodes.

server3 `/tmp`: 291974778880 available bytes; 83.71% used; 114174951 free inodes.

server3 `/var/tmp`: 291974778880 available bytes; 83.71% used; 114174951 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105792921600 available bytes; 94.10% used; 114349570 free inodes.

server4 `/home`: 105792921600 available bytes; 94.10% used; 114349570 free inodes.

server4 `/data`: 277934637056 available bytes; 96.16% used; 225384318 free inodes.

server4 `/tmp`: 105792921600 available bytes; 94.10% used; 114349570 free inodes.

server4 `/var/tmp`: 105792921600 available bytes; 94.10% used; 114349570 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
