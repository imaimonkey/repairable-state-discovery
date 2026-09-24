# V2R cluster inventory

2026-09-24T08:41:01.099050+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324392521728 available bytes; 81.90% used; 112490358 free inodes.

server1 `/home`: 324392521728 available bytes; 81.90% used; 112490358 free inodes.

server1 `/tmp`: 324392521728 available bytes; 81.90% used; 112490358 free inodes.

server1 `/var/tmp`: 324392521728 available bytes; 81.90% used; 112490358 free inodes.

server1 `/mnt/raid5`: 506154258432 available bytes; 97.68% used; 337719305 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57798533120 available bytes; 96.78% used; 110430970 free inodes.

server2 `/home`: 57798533120 available bytes; 96.78% used; 110430970 free inodes.

server2 `/tmp`: 57798533120 available bytes; 96.78% used; 110430970 free inodes.

server2 `/var/tmp`: 57798533120 available bytes; 96.78% used; 110430970 free inodes.

server2 `/mnt/raid5`: 515806679040 available bytes; 96.44% used; 445179243 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85411344384 available bytes; 95.23% used; 114171929 free inodes.

server3 `/home`: 85411344384 available bytes; 95.23% used; 114171929 free inodes.

server3 `/data`: 173663608832 available bytes; 97.60% used; 225822311 free inodes.

server3 `/tmp`: 85411344384 available bytes; 95.23% used; 114171929 free inodes.

server3 `/var/tmp`: 85411344384 available bytes; 95.23% used; 114171929 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105768689664 available bytes; 94.10% used; 114349092 free inodes.

server4 `/home`: 105768689664 available bytes; 94.10% used; 114349092 free inodes.

server4 `/data`: 255370964992 available bytes; 96.47% used; 225288355 free inodes.

server4 `/tmp`: 105768689664 available bytes; 94.10% used; 114349092 free inodes.

server4 `/var/tmp`: 105768689664 available bytes; 94.10% used; 114349092 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
