# V2R cluster inventory

2026-09-24T00:47:26.712255+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325536329728 available bytes; 81.84% used; 112500412 free inodes.

server1 `/home`: 325536329728 available bytes; 81.84% used; 112500412 free inodes.

server1 `/tmp`: 325536329728 available bytes; 81.84% used; 112500412 free inodes.

server1 `/var/tmp`: 325536329728 available bytes; 81.84% used; 112500412 free inodes.

server1 `/mnt/raid5`: 1071574757376 available bytes; 95.08% used; 337734972 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40980668416 available bytes; 97.71% used; 110432271 free inodes.

server2 `/home`: 40980668416 available bytes; 97.71% used; 110432271 free inodes.

server2 `/tmp`: 40980668416 available bytes; 97.71% used; 110432271 free inodes.

server2 `/var/tmp`: 40980668416 available bytes; 97.71% used; 110432271 free inodes.

server2 `/mnt/raid5`: 532245090304 available bytes; 96.32% used; 445202906 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292341977088 available bytes; 83.69% used; 114188827 free inodes.

server3 `/home`: 292341977088 available bytes; 83.69% used; 114188827 free inodes.

server3 `/data`: 82216349696 available bytes; 98.86% used; 225843561 free inodes.

server3 `/tmp`: 292341977088 available bytes; 83.69% used; 114188827 free inodes.

server3 `/var/tmp`: 292341977088 available bytes; 83.69% used; 114188827 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106050633728 available bytes; 94.08% used; 114349890 free inodes.

server4 `/home`: 106050633728 available bytes; 94.08% used; 114349890 free inodes.

server4 `/data`: 292918538240 available bytes; 95.95% used; 225414576 free inodes.

server4 `/tmp`: 106050633728 available bytes; 94.08% used; 114349890 free inodes.

server4 `/var/tmp`: 106050633728 available bytes; 94.08% used; 114349890 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
