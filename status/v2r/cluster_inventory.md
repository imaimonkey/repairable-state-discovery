# V2R cluster inventory

2026-09-24T11:22:54.466170+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324353089536 available bytes; 81.91% used; 112488882 free inodes.

server1 `/home`: 324353089536 available bytes; 81.91% used; 112488882 free inodes.

server1 `/tmp`: 324353089536 available bytes; 81.91% used; 112488882 free inodes.

server1 `/var/tmp`: 324353089536 available bytes; 81.91% used; 112488882 free inodes.

server1 `/mnt/raid5`: 453164847104 available bytes; 97.92% used; 337690142 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57671643136 available bytes; 96.78% used; 110430072 free inodes.

server2 `/home`: 57671643136 available bytes; 96.78% used; 110430072 free inodes.

server2 `/tmp`: 57671643136 available bytes; 96.78% used; 110430072 free inodes.

server2 `/var/tmp`: 57671643136 available bytes; 96.78% used; 110430072 free inodes.

server2 `/mnt/raid5`: 510861275136 available bytes; 96.47% used; 445173567 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85757575168 available bytes; 95.21% used; 114197366 free inodes.

server3 `/home`: 85757575168 available bytes; 95.21% used; 114197366 free inodes.

server3 `/data`: 163854655488 available bytes; 97.74% used; 225816793 free inodes.

server3 `/tmp`: 85757575168 available bytes; 95.21% used; 114197366 free inodes.

server3 `/var/tmp`: 85757575168 available bytes; 95.21% used; 114197366 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731125248 available bytes; 94.10% used; 114348877 free inodes.

server4 `/home`: 105731125248 available bytes; 94.10% used; 114348877 free inodes.

server4 `/data`: 115642830848 available bytes; 98.40% used; 225258075 free inodes.

server4 `/tmp`: 105731125248 available bytes; 94.10% used; 114348877 free inodes.

server4 `/var/tmp`: 105731125248 available bytes; 94.10% used; 114348877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
