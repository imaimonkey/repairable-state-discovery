# V2R cluster inventory

2026-09-25T11:59:08.689108+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319047225344 available bytes; 82.20% used; 112478828 free inodes.

server1 `/home`: 319047225344 available bytes; 82.20% used; 112478828 free inodes.

server1 `/tmp`: 319047225344 available bytes; 82.20% used; 112478828 free inodes.

server1 `/var/tmp`: 319047221248 available bytes; 82.20% used; 112478828 free inodes.

server1 `/mnt/raid5`: 371520122880 available bytes; 98.30% used; 337549232 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22910877696 available bytes; 98.72% used; 110409974 free inodes.

server2 `/home`: 22910877696 available bytes; 98.72% used; 110409974 free inodes.

server2 `/tmp`: 22910877696 available bytes; 98.72% used; 110409974 free inodes.

server2 `/var/tmp`: 22910877696 available bytes; 98.72% used; 110409974 free inodes.

server2 `/mnt/raid5`: 326066835456 available bytes; 97.75% used; 445082072 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84214632448 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84214632448 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142122680320 available bytes; 98.04% used; 225812650 free inodes.

server3 `/tmp`: 84214632448 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84214632448 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105593815040 available bytes; 94.11% used; 114350234 free inodes.

server4 `/home`: 105593815040 available bytes; 94.11% used; 114350234 free inodes.

server4 `/data`: 232648638464 available bytes; 96.78% used; 224972926 free inodes.

server4 `/tmp`: 105593815040 available bytes; 94.11% used; 114350234 free inodes.

server4 `/var/tmp`: 105593815040 available bytes; 94.11% used; 114350234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
