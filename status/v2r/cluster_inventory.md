# V2R cluster inventory

2026-09-25T13:42:01.041583+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319185735680 available bytes; 82.19% used; 112477015 free inodes.

server1 `/home`: 319185735680 available bytes; 82.19% used; 112477015 free inodes.

server1 `/tmp`: 319185735680 available bytes; 82.19% used; 112477015 free inodes.

server1 `/var/tmp`: 319185735680 available bytes; 82.19% used; 112477015 free inodes.

server1 `/mnt/raid5`: 364156485632 available bytes; 98.33% used; 337547681 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 16531443712 available bytes; 99.08% used; 110408634 free inodes.

server2 `/home`: 16531443712 available bytes; 99.08% used; 110408634 free inodes.

server2 `/tmp`: 16531443712 available bytes; 99.08% used; 110408634 free inodes.

server2 `/var/tmp`: 16531443712 available bytes; 99.08% used; 110408634 free inodes.

server2 `/mnt/raid5`: 323123200000 available bytes; 97.77% used; 445077101 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84281819136 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84281819136 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142346227712 available bytes; 98.03% used; 225809503 free inodes.

server3 `/tmp`: 84281819136 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84281819136 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655648256 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655648256 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231463673856 available bytes; 96.80% used; 224950340 free inodes.

server4 `/tmp`: 105655648256 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655648256 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
