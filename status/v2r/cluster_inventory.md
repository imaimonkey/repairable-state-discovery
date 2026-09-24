# V2R cluster inventory

2026-09-24T03:48:25.517285+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324739981312 available bytes; 81.88% used; 112493708 free inodes.

server1 `/home`: 324739981312 available bytes; 81.88% used; 112493708 free inodes.

server1 `/tmp`: 324739981312 available bytes; 81.88% used; 112493708 free inodes.

server1 `/var/tmp`: 324739981312 available bytes; 81.88% used; 112493708 free inodes.

server1 `/mnt/raid5`: 406966095872 available bytes; 98.13% used; 337724828 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40818683904 available bytes; 97.72% used; 110430956 free inodes.

server2 `/home`: 40818683904 available bytes; 97.72% used; 110430956 free inodes.

server2 `/tmp`: 40818683904 available bytes; 97.72% used; 110430956 free inodes.

server2 `/var/tmp`: 40818683904 available bytes; 97.72% used; 110430956 free inodes.

server2 `/mnt/raid5`: 526645665792 available bytes; 96.36% used; 445197149 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292363087872 available bytes; 83.69% used; 114197805 free inodes.

server3 `/home`: 292363087872 available bytes; 83.69% used; 114197805 free inodes.

server3 `/data`: 33876357120 available bytes; 99.53% used; 225842652 free inodes.

server3 `/tmp`: 292363087872 available bytes; 83.69% used; 114197805 free inodes.

server3 `/var/tmp`: 292363087872 available bytes; 83.69% used; 114197805 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105792577536 available bytes; 94.10% used; 114349565 free inodes.

server4 `/home`: 105792577536 available bytes; 94.10% used; 114349565 free inodes.

server4 `/data`: 276085121024 available bytes; 96.18% used; 225384173 free inodes.

server4 `/tmp`: 105792577536 available bytes; 94.10% used; 114349565 free inodes.

server4 `/var/tmp`: 105792577536 available bytes; 94.10% used; 114349565 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
