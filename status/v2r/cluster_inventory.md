# V2R cluster inventory

2026-09-24T11:10:16.867668+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324367020032 available bytes; 81.90% used; 112488969 free inodes.

server1 `/home`: 324367020032 available bytes; 81.90% used; 112488969 free inodes.

server1 `/tmp`: 324367020032 available bytes; 81.90% used; 112488969 free inodes.

server1 `/var/tmp`: 324367020032 available bytes; 81.90% used; 112488969 free inodes.

server1 `/mnt/raid5`: 474356039680 available bytes; 97.82% used; 337692135 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 57684426752 available bytes; 96.78% used; 110430195 free inodes.

server2 `/home`: 57684426752 available bytes; 96.78% used; 110430195 free inodes.

server2 `/tmp`: 57684426752 available bytes; 96.78% used; 110430195 free inodes.

server2 `/var/tmp`: 57684426752 available bytes; 96.78% used; 110430195 free inodes.

server2 `/mnt/raid5`: 511528779776 available bytes; 96.47% used; 445174218 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85765181440 available bytes; 95.21% used; 114198729 free inodes.

server3 `/home`: 85765181440 available bytes; 95.21% used; 114198729 free inodes.

server3 `/data`: 163943104512 available bytes; 97.73% used; 225817049 free inodes.

server3 `/tmp`: 85765181440 available bytes; 95.21% used; 114198729 free inodes.

server3 `/var/tmp`: 85765181440 available bytes; 95.21% used; 114198729 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105733480448 available bytes; 94.10% used; 114348921 free inodes.

server4 `/home`: 105733480448 available bytes; 94.10% used; 114348921 free inodes.

server4 `/data`: 115731730432 available bytes; 98.40% used; 225258197 free inodes.

server4 `/tmp`: 105733480448 available bytes; 94.10% used; 114348921 free inodes.

server4 `/var/tmp`: 105733480448 available bytes; 94.10% used; 114348921 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
