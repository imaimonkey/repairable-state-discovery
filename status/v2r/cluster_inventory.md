# V2R cluster inventory

2026-09-25T13:52:42.001113+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319151058944 available bytes; 82.20% used; 112476961 free inodes.

server1 `/home`: 319151058944 available bytes; 82.20% used; 112476961 free inodes.

server1 `/tmp`: 319151058944 available bytes; 82.20% used; 112476961 free inodes.

server1 `/var/tmp`: 319151058944 available bytes; 82.20% used; 112476961 free inodes.

server1 `/mnt/raid5`: 364094607360 available bytes; 98.33% used; 337547530 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4727128064 available bytes; 99.74% used; 110407473 free inodes.

server2 `/home`: 4727128064 available bytes; 99.74% used; 110407473 free inodes.

server2 `/tmp`: 4727128064 available bytes; 99.74% used; 110407473 free inodes.

server2 `/var/tmp`: 4727128064 available bytes; 99.74% used; 110407473 free inodes.

server2 `/mnt/raid5`: 322532749312 available bytes; 97.77% used; 445076551 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84280664064 available bytes; 95.30% used; 114154466 free inodes.

server3 `/home`: 84280664064 available bytes; 95.30% used; 114154466 free inodes.

server3 `/data`: 142291156992 available bytes; 98.03% used; 225809332 free inodes.

server3 `/tmp`: 84280664064 available bytes; 95.30% used; 114154466 free inodes.

server3 `/var/tmp`: 84280664064 available bytes; 95.30% used; 114154466 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655341056 available bytes; 94.10% used; 114349713 free inodes.

server4 `/home`: 105655341056 available bytes; 94.10% used; 114349713 free inodes.

server4 `/data`: 231435325440 available bytes; 96.80% used; 224949551 free inodes.

server4 `/tmp`: 105655341056 available bytes; 94.10% used; 114349713 free inodes.

server4 `/var/tmp`: 105655341056 available bytes; 94.10% used; 114349713 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
