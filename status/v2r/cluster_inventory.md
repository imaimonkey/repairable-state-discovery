# V2R cluster inventory

2026-09-24T02:41:32.606166+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325384404992 available bytes; 81.85% used; 112498758 free inodes.

server1 `/home`: 325384404992 available bytes; 81.85% used; 112498758 free inodes.

server1 `/tmp`: 325384404992 available bytes; 81.85% used; 112498758 free inodes.

server1 `/var/tmp`: 325384404992 available bytes; 81.85% used; 112498758 free inodes.

server1 `/mnt/raid5`: 598704861184 available bytes; 97.25% used; 337733183 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40877817856 available bytes; 97.72% used; 110431452 free inodes.

server2 `/home`: 40877817856 available bytes; 97.72% used; 110431452 free inodes.

server2 `/tmp`: 40877817856 available bytes; 97.72% used; 110431452 free inodes.

server2 `/var/tmp`: 40877817856 available bytes; 97.72% used; 110431452 free inodes.

server2 `/mnt/raid5`: 528661360640 available bytes; 96.35% used; 445199286 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292683292672 available bytes; 83.67% used; 114210613 free inodes.

server3 `/home`: 292683292672 available bytes; 83.67% used; 114210613 free inodes.

server3 `/data`: 39737667584 available bytes; 99.45% used; 225846104 free inodes.

server3 `/tmp`: 292683292672 available bytes; 83.67% used; 114210613 free inodes.

server3 `/var/tmp`: 292683292672 available bytes; 83.67% used; 114210613 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003140608 available bytes; 94.08% used; 114349830 free inodes.

server4 `/home`: 106003140608 available bytes; 94.08% used; 114349830 free inodes.

server4 `/data`: 289734737920 available bytes; 96.00% used; 225387287 free inodes.

server4 `/tmp`: 106003140608 available bytes; 94.08% used; 114349830 free inodes.

server4 `/var/tmp`: 106003140608 available bytes; 94.08% used; 114349830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
