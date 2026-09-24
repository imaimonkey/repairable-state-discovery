# V2R cluster inventory

2026-09-24T08:37:55.159289+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324395327488 available bytes; 81.90% used; 112490384 free inodes.

server1 `/home`: 324395327488 available bytes; 81.90% used; 112490384 free inodes.

server1 `/tmp`: 324395327488 available bytes; 81.90% used; 112490384 free inodes.

server1 `/var/tmp`: 324395327488 available bytes; 81.90% used; 112490384 free inodes.

server1 `/mnt/raid5`: 507377537024 available bytes; 97.67% used; 337719712 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57800044544 available bytes; 96.78% used; 110430976 free inodes.

server2 `/home`: 57800044544 available bytes; 96.78% used; 110430976 free inodes.

server2 `/tmp`: 57800044544 available bytes; 96.78% used; 110430976 free inodes.

server2 `/var/tmp`: 57800044544 available bytes; 96.78% used; 110430976 free inodes.

server2 `/mnt/raid5`: 515906514944 available bytes; 96.44% used; 445179368 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85481467904 available bytes; 95.23% used; 114174916 free inodes.

server3 `/home`: 85481467904 available bytes; 95.23% used; 114174916 free inodes.

server3 `/data`: 173696798720 available bytes; 97.60% used; 225822723 free inodes.

server3 `/tmp`: 85481467904 available bytes; 95.23% used; 114174916 free inodes.

server3 `/var/tmp`: 85481467904 available bytes; 95.23% used; 114174916 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105768820736 available bytes; 94.10% used; 114349092 free inodes.

server4 `/home`: 105768820736 available bytes; 94.10% used; 114349092 free inodes.

server4 `/data`: 255373090816 available bytes; 96.47% used; 225288371 free inodes.

server4 `/tmp`: 105768820736 available bytes; 94.10% used; 114349092 free inodes.

server4 `/var/tmp`: 105768820736 available bytes; 94.10% used; 114349092 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
