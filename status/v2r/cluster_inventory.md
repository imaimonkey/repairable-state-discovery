# V2R cluster inventory

2026-09-24T02:43:54.270340+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325381812224 available bytes; 81.85% used; 112498728 free inodes.

server1 `/home`: 325381812224 available bytes; 81.85% used; 112498728 free inodes.

server1 `/tmp`: 325381812224 available bytes; 81.85% used; 112498728 free inodes.

server1 `/var/tmp`: 325381812224 available bytes; 81.85% used; 112498728 free inodes.

server1 `/mnt/raid5`: 588683907072 available bytes; 97.30% used; 337733165 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40877289472 available bytes; 97.72% used; 110431438 free inodes.

server2 `/home`: 40877289472 available bytes; 97.72% used; 110431438 free inodes.

server2 `/tmp`: 40877289472 available bytes; 97.72% used; 110431438 free inodes.

server2 `/var/tmp`: 40877289472 available bytes; 97.72% used; 110431438 free inodes.

server2 `/mnt/raid5`: 528577830912 available bytes; 96.35% used; 445199071 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292694712320 available bytes; 83.67% used; 114210665 free inodes.

server3 `/home`: 292694712320 available bytes; 83.67% used; 114210665 free inodes.

server3 `/data`: 39736877056 available bytes; 99.45% used; 225846061 free inodes.

server3 `/tmp`: 292694712320 available bytes; 83.67% used; 114210665 free inodes.

server3 `/var/tmp`: 292694712320 available bytes; 83.67% used; 114210665 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106003030016 available bytes; 94.08% used; 114349830 free inodes.

server4 `/home`: 106003030016 available bytes; 94.08% used; 114349830 free inodes.

server4 `/data`: 289730211840 available bytes; 96.00% used; 225387235 free inodes.

server4 `/tmp`: 106003030016 available bytes; 94.08% used; 114349830 free inodes.

server4 `/var/tmp`: 106003030016 available bytes; 94.08% used; 114349830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
