# V2R cluster inventory

2026-09-26T20:25:27.854953+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315482374144 available bytes; 82.40% used; 112444698 free inodes.

server1 `/home`: 315482374144 available bytes; 82.40% used; 112444698 free inodes.

server1 `/tmp`: 315482374144 available bytes; 82.40% used; 112444698 free inodes.

server1 `/var/tmp`: 315482374144 available bytes; 82.40% used; 112444698 free inodes.

server1 `/mnt/raid5`: 645853995008 available bytes; 97.04% used; 337467117 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17982701568 available bytes; 99.00% used; 110367107 free inodes.

server2 `/home`: 17982701568 available bytes; 99.00% used; 110367107 free inodes.

server2 `/tmp`: 17982701568 available bytes; 99.00% used; 110367107 free inodes.

server2 `/var/tmp`: 17982701568 available bytes; 99.00% used; 110367107 free inodes.

server2 `/mnt/raid5`: 600820793344 available bytes; 95.85% used; 444964657 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81263357952 available bytes; 95.47% used; 114065299 free inodes.

server3 `/home`: 81263357952 available bytes; 95.47% used; 114065299 free inodes.

server3 `/data`: 1348625362944 available bytes; 81.36% used; 225831949 free inodes.

server3 `/tmp`: 81263357952 available bytes; 95.47% used; 114065299 free inodes.

server3 `/var/tmp`: 81263357952 available bytes; 95.47% used; 114065299 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105919164416 available bytes; 94.09% used; 114347833 free inodes.

server4 `/home`: 105919164416 available bytes; 94.09% used; 114347833 free inodes.

server4 `/data`: 410202931200 available bytes; 94.33% used; 224823722 free inodes.

server4 `/tmp`: 105919164416 available bytes; 94.09% used; 114347833 free inodes.

server4 `/var/tmp`: 105919164416 available bytes; 94.09% used; 114347833 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
