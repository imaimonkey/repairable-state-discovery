# V2R cluster inventory

2026-09-25T13:14:24.263868+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319110443008 available bytes; 82.20% used; 112477572 free inodes.

server1 `/home`: 319110443008 available bytes; 82.20% used; 112477572 free inodes.

server1 `/tmp`: 319110443008 available bytes; 82.20% used; 112477572 free inodes.

server1 `/var/tmp`: 319110443008 available bytes; 82.20% used; 112477572 free inodes.

server1 `/mnt/raid5`: 364260589568 available bytes; 98.33% used; 337547903 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8217055232 available bytes; 99.54% used; 110408758 free inodes.

server2 `/home`: 8217055232 available bytes; 99.54% used; 110408758 free inodes.

server2 `/tmp`: 8217051136 available bytes; 99.54% used; 110408758 free inodes.

server2 `/var/tmp`: 8217047040 available bytes; 99.54% used; 110408758 free inodes.

server2 `/mnt/raid5`: 323906506752 available bytes; 97.76% used; 445077408 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84207464448 available bytes; 95.30% used; 114154970 free inodes.

server3 `/home`: 84207464448 available bytes; 95.30% used; 114154970 free inodes.

server3 `/data`: 142351638528 available bytes; 98.03% used; 225809971 free inodes.

server3 `/tmp`: 84207464448 available bytes; 95.30% used; 114154970 free inodes.

server3 `/var/tmp`: 84207464448 available bytes; 95.30% used; 114154970 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656406016 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656406016 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231420436480 available bytes; 96.80% used; 224953720 free inodes.

server4 `/tmp`: 105656406016 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656406016 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
