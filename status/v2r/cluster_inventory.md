# V2R cluster inventory

2026-09-24T02:38:26.263593+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325383356416 available bytes; 81.85% used; 112498784 free inodes.

server1 `/home`: 325383356416 available bytes; 81.85% used; 112498784 free inodes.

server1 `/tmp`: 325383356416 available bytes; 81.85% used; 112498784 free inodes.

server1 `/var/tmp`: 325383356416 available bytes; 81.85% used; 112498784 free inodes.

server1 `/mnt/raid5`: 611907555328 available bytes; 97.19% used; 337733238 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40880910336 available bytes; 97.72% used; 110431476 free inodes.

server2 `/home`: 40880910336 available bytes; 97.72% used; 110431476 free inodes.

server2 `/tmp`: 40880910336 available bytes; 97.72% used; 110431476 free inodes.

server2 `/var/tmp`: 40880910336 available bytes; 97.72% used; 110431476 free inodes.

server2 `/mnt/raid5`: 528750481408 available bytes; 96.35% used; 445199386 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292680630272 available bytes; 83.67% used; 114210613 free inodes.

server3 `/home`: 292680630272 available bytes; 83.67% used; 114210613 free inodes.

server3 `/data`: 39742828544 available bytes; 99.45% used; 225846168 free inodes.

server3 `/tmp`: 292680630272 available bytes; 83.67% used; 114210613 free inodes.

server3 `/var/tmp`: 292680630272 available bytes; 83.67% used; 114210613 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003300352 available bytes; 94.08% used; 114349834 free inodes.

server4 `/home`: 106003300352 available bytes; 94.08% used; 114349834 free inodes.

server4 `/data`: 289736515584 available bytes; 96.00% used; 225387358 free inodes.

server4 `/tmp`: 106003300352 available bytes; 94.08% used; 114349834 free inodes.

server4 `/var/tmp`: 106003300352 available bytes; 94.08% used; 114349834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
