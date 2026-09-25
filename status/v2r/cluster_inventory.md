# V2R cluster inventory

2026-09-25T12:17:48.247210+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319200698368 available bytes; 82.19% used; 112477787 free inodes.

server1 `/home`: 319200698368 available bytes; 82.19% used; 112477787 free inodes.

server1 `/tmp`: 319200698368 available bytes; 82.19% used; 112477787 free inodes.

server1 `/var/tmp`: 319200698368 available bytes; 82.19% used; 112477787 free inodes.

server1 `/mnt/raid5`: 364310810624 available bytes; 98.33% used; 337548273 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22903234560 available bytes; 98.72% used; 110409959 free inodes.

server2 `/home`: 22903234560 available bytes; 98.72% used; 110409959 free inodes.

server2 `/tmp`: 22903234560 available bytes; 98.72% used; 110409959 free inodes.

server2 `/var/tmp`: 22903234560 available bytes; 98.72% used; 110409959 free inodes.

server2 `/mnt/raid5`: 325312417792 available bytes; 97.75% used; 445080848 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84210946048 available bytes; 95.30% used; 114154984 free inodes.

server3 `/home`: 84210946048 available bytes; 95.30% used; 114154984 free inodes.

server3 `/data`: 142283214848 available bytes; 98.03% used; 225811325 free inodes.

server3 `/tmp`: 84210946048 available bytes; 95.30% used; 114154984 free inodes.

server3 `/var/tmp`: 84210946048 available bytes; 95.30% used; 114154984 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105666510848 available bytes; 94.10% used; 114349722 free inodes.

server4 `/home`: 105666510848 available bytes; 94.10% used; 114349722 free inodes.

server4 `/data`: 232052629504 available bytes; 96.79% used; 224966041 free inodes.

server4 `/tmp`: 105666510848 available bytes; 94.10% used; 114349722 free inodes.

server4 `/var/tmp`: 105666510848 available bytes; 94.10% used; 114349722 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
