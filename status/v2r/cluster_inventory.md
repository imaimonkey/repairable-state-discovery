# V2R cluster inventory

2026-09-27T03:59:21.545061+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315074523136 available bytes; 82.42% used; 112443035 free inodes.

server1 `/home`: 315074523136 available bytes; 82.42% used; 112443035 free inodes.

server1 `/tmp`: 315074523136 available bytes; 82.42% used; 112443035 free inodes.

server1 `/var/tmp`: 315074523136 available bytes; 82.42% used; 112443035 free inodes.

server1 `/mnt/raid5`: 636784369664 available bytes; 97.08% used; 337401377 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17625153536 available bytes; 99.02% used; 110365009 free inodes.

server2 `/home`: 17625153536 available bytes; 99.02% used; 110365009 free inodes.

server2 `/tmp`: 17625153536 available bytes; 99.02% used; 110365009 free inodes.

server2 `/var/tmp`: 17625153536 available bytes; 99.02% used; 110365009 free inodes.

server2 `/mnt/raid5`: 577871130624 available bytes; 96.01% used; 444882768 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78696472576 available bytes; 95.61% used; 114062929 free inodes.

server3 `/home`: 78696472576 available bytes; 95.61% used; 114062929 free inodes.

server3 `/data`: 1335209504768 available bytes; 81.55% used; 225759796 free inodes.

server3 `/tmp`: 78696472576 available bytes; 95.61% used; 114062929 free inodes.

server3 `/var/tmp`: 78696472576 available bytes; 95.61% used; 114062929 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111027281920 available bytes; 93.80% used; 114372943 free inodes.

server4 `/home`: 111027281920 available bytes; 93.80% used; 114372943 free inodes.

server4 `/data`: 382184259584 available bytes; 94.72% used; 224780795 free inodes.

server4 `/tmp`: 111027281920 available bytes; 93.80% used; 114372943 free inodes.

server4 `/var/tmp`: 111027281920 available bytes; 93.80% used; 114372943 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
